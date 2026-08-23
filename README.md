# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 348
- HTTP: 104 alive / 41 gold
- HTTPS: 47 alive / 8 gold
- SOCKS4: 163 alive / 155 gold
- SOCKS5: 162 alive / 144 gold

## Historical pool

- Discovered: 171068
- Ever alive: 32860
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
