# SyndProxy private pool

## Current pool

- Alive now: 1141
- Gold now: 470
- HTTP: 429 alive / 125 gold
- HTTPS: 258 alive / 70 gold
- SOCKS4: 200 alive / 131 gold
- SOCKS5: 254 alive / 144 gold

## Historical pool

- Discovered: 117107
- Ever alive: 17182
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
