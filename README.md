# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 466
- HTTP: 134 alive / 94 gold
- HTTPS: 60 alive / 34 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 192 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49395
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
