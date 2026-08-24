# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 387
- HTTP: 129 alive / 54 gold
- HTTPS: 44 alive / 12 gold
- SOCKS4: 176 alive / 157 gold
- SOCKS5: 197 alive / 164 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33374
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
