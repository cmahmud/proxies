# SyndProxy validated proxy pool

## Current pool

- Alive now: 657
- Gold now: 418
- HTTP: 144 alive / 79 gold
- HTTPS: 162 alive / 26 gold
- SOCKS4: 163 alive / 152 gold
- SOCKS5: 188 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40271
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
