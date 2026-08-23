# SyndProxy validated proxy pool

## Current pool

- Alive now: 465
- Gold now: 349
- HTTP: 100 alive / 42 gold
- HTTPS: 42 alive / 8 gold
- SOCKS4: 160 alive / 155 gold
- SOCKS5: 163 alive / 144 gold

## Historical pool

- Discovered: 171068
- Ever alive: 32860
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
