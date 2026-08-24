# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 379
- HTTP: 112 alive / 47 gold
- HTTPS: 45 alive / 8 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 181 alive / 164 gold

## Historical pool

- Discovered: 180671
- Ever alive: 33579
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
