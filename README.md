# SyndProxy private pool

## Current pool

- Alive now: 631
- Gold now: 384
- HTTP: 157 alive / 67 gold
- HTTPS: 84 alive / 17 gold
- SOCKS4: 194 alive / 150 gold
- SOCKS5: 196 alive / 150 gold

## Historical pool

- Discovered: 146659
- Ever alive: 25706
- Ever gold: 1072

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
