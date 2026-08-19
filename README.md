# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 501
- HTTP: 340 alive / 142 gold
- HTTPS: 237 alive / 80 gold
- SOCKS4: 243 alive / 147 gold
- SOCKS5: 211 alive / 132 gold

## Historical pool

- Discovered: 119697
- Ever alive: 17907
- Ever gold: 705

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
