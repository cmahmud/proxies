# SyndProxy private pool

## Current pool

- Alive now: 966
- Gold now: 392
- HTTP: 330 alive / 87 gold
- HTTPS: 177 alive / 19 gold
- SOCKS4: 204 alive / 128 gold
- SOCKS5: 255 alive / 158 gold

## Historical pool

- Discovered: 157412
- Ever alive: 29707
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
