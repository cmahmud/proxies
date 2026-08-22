# SyndProxy private pool

## Current pool

- Alive now: 967
- Gold now: 420
- HTTP: 265 alive / 80 gold
- HTTPS: 243 alive / 26 gold
- SOCKS4: 209 alive / 142 gold
- SOCKS5: 250 alive / 172 gold

## Historical pool

- Discovered: 161931
- Ever alive: 31213
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
