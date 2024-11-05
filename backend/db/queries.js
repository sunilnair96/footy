// backend/db/queries.js
import { query } from "./db"; // Import your query function

export const getAllSeasons = async () => {
  return await query("SELECT * FROM seasons");
};
