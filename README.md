# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 389
- HTTP: 98 alive / 55 gold
- HTTPS: 33 alive / 12 gold
- SOCKS4: 168 alive / 157 gold
- SOCKS5: 192 alive / 165 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33389
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
