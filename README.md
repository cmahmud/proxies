# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 424
- HTTP: 114 alive / 72 gold
- HTTPS: 99 alive / 24 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 183 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34914
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
