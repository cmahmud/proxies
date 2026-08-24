# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 375
- HTTP: 115 alive / 43 gold
- HTTPS: 48 alive / 9 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 181 alive / 163 gold

## Historical pool

- Discovered: 180671
- Ever alive: 33579
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
