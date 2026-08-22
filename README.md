# SyndProxy private pool

## Current pool

- Alive now: 1114
- Gold now: 423
- HTTP: 394 alive / 99 gold
- HTTPS: 282 alive / 32 gold
- SOCKS4: 195 alive / 135 gold
- SOCKS5: 243 alive / 157 gold

## Historical pool

- Discovered: 161019
- Ever alive: 31115
- Ever gold: 1154

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
