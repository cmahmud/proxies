# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 413
- HTTP: 107 alive / 72 gold
- HTTPS: 117 alive / 23 gold
- SOCKS4: 163 alive / 157 gold
- SOCKS5: 181 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41877
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
