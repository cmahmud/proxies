# SyndProxy validated proxy pool

## Current pool

- Alive now: 709
- Gold now: 198
- HTTP: 224 alive / 35 gold
- HTTPS: 43 alive / 6 gold
- SOCKS4: 188 alive / 69 gold
- SOCKS5: 254 alive / 88 gold

## Historical pool

- Discovered: 170566
- Ever alive: 32778
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
