# SyndProxy private pool

## Current pool

- Alive now: 1606
- Gold now: 656
- HTTP: 624 alive / 221 gold
- HTTPS: 490 alive / 108 gold
- SOCKS4: 238 alive / 154 gold
- SOCKS5: 254 alive / 173 gold

## Historical pool

- Discovered: 141227
- Ever alive: 23985
- Ever gold: 967

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
