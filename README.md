# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 420
- HTTP: 89 alive / 65 gold
- HTTPS: 89 alive / 24 gold
- SOCKS4: 164 alive / 160 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35641
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
