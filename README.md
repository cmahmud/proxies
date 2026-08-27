# SyndProxy validated proxy pool

## Current pool

- Alive now: 674
- Gold now: 420
- HTTP: 116 alive / 73 gold
- HTTPS: 181 alive / 18 gold
- SOCKS4: 192 alive / 163 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41195
- Ever gold: 1318

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
