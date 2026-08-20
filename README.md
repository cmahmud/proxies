# SyndProxy private pool

## Current pool

- Alive now: 1603
- Gold now: 644
- HTTP: 627 alive / 240 gold
- HTTPS: 520 alive / 128 gold
- SOCKS4: 212 alive / 133 gold
- SOCKS5: 244 alive / 143 gold

## Historical pool

- Discovered: 142727
- Ever alive: 24533
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
