# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 463
- HTTP: 127 alive / 92 gold
- HTTPS: 53 alive / 36 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49402
- Ever gold: 1580

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
