# SyndProxy validated proxy pool

## Current pool

- Alive now: 657
- Gold now: 398
- HTTP: 142 alive / 74 gold
- HTTPS: 170 alive / 24 gold
- SOCKS4: 162 alive / 146 gold
- SOCKS5: 183 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40016
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
