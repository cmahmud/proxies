# SyndProxy validated proxy pool

## Current pool

- Alive now: 662
- Gold now: 419
- HTTP: 146 alive / 79 gold
- HTTPS: 163 alive / 26 gold
- SOCKS4: 164 alive / 153 gold
- SOCKS5: 189 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40275
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
