# SyndProxy private pool

## Current pool

- Alive now: 1310
- Gold now: 565
- HTTP: 538 alive / 193 gold
- HTTPS: 345 alive / 97 gold
- SOCKS4: 223 alive / 143 gold
- SOCKS5: 204 alive / 132 gold

## Historical pool

- Discovered: 136255
- Ever alive: 22786
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
