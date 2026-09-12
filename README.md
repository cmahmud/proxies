# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 440
- HTTP: 114 alive / 88 gold
- HTTPS: 58 alive / 31 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49440
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
