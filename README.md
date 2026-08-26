# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 411
- HTTP: 129 alive / 77 gold
- HTTPS: 148 alive / 22 gold
- SOCKS4: 164 alive / 154 gold
- SOCKS5: 183 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40225
- Ever gold: 1308

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
