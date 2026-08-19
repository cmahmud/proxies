# SyndProxy private pool

## Current pool

- Alive now: 1215
- Gold now: 526
- HTTP: 443 alive / 182 gold
- HTTPS: 333 alive / 63 gold
- SOCKS4: 200 alive / 122 gold
- SOCKS5: 239 alive / 159 gold

## Historical pool

- Discovered: 125606
- Ever alive: 19593
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
