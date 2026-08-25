# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 413
- HTTP: 85 alive / 57 gold
- HTTPS: 72 alive / 21 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 190 alive / 172 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36266
- Ever gold: 1270

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
