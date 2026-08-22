# SyndProxy private pool

## Current pool

- Alive now: 978
- Gold now: 421
- HTTP: 266 alive / 81 gold
- HTTPS: 262 alive / 25 gold
- SOCKS4: 206 alive / 143 gold
- SOCKS5: 244 alive / 172 gold

## Historical pool

- Discovered: 161927
- Ever alive: 31210
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
