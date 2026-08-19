# SyndProxy private pool

## Current pool

- Alive now: 1049
- Gold now: 503
- HTTP: 351 alive / 144 gold
- HTTPS: 254 alive / 80 gold
- SOCKS4: 240 alive / 147 gold
- SOCKS5: 204 alive / 132 gold

## Historical pool

- Discovered: 119808
- Ever alive: 17940
- Ever gold: 705

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
