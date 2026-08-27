# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 404
- HTTP: 119 alive / 62 gold
- HTTPS: 158 alive / 11 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 187 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40863
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
