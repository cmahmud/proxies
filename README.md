# SyndProxy private pool

## Current pool

- Alive now: 820
- Gold now: 410
- HTTP: 220 alive / 84 gold
- HTTPS: 142 alive / 21 gold
- SOCKS4: 219 alive / 153 gold
- SOCKS5: 239 alive / 152 gold

## Historical pool

- Discovered: 155685
- Ever alive: 29213
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
