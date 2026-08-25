# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 420
- HTTP: 87 alive / 64 gold
- HTTPS: 92 alive / 22 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 191 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36085
- Ever gold: 1267

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
