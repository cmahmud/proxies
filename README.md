# SyndProxy private pool

## Current pool

- Alive now: 978
- Gold now: 421
- HTTP: 300 alive / 107 gold
- HTTPS: 186 alive / 29 gold
- SOCKS4: 230 alive / 148 gold
- SOCKS5: 262 alive / 137 gold

## Historical pool

- Discovered: 160279
- Ever alive: 30804
- Ever gold: 1149

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
