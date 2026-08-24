# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 383
- HTTP: 92 alive / 44 gold
- HTTPS: 59 alive / 14 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 181 alive / 164 gold

## Historical pool

- Discovered: 180671
- Ever alive: 33578
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
