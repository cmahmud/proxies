# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 412
- HTTP: 121 alive / 63 gold
- HTTPS: 170 alive / 16 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 184 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40805
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
