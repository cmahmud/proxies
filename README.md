# SyndProxy private pool

## Current pool

- Alive now: 852
- Gold now: 345
- HTTP: 282 alive / 83 gold
- HTTPS: 153 alive / 22 gold
- SOCKS4: 194 alive / 113 gold
- SOCKS5: 223 alive / 127 gold

## Historical pool

- Discovered: 167410
- Ever alive: 32580
- Ever gold: 1190

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
