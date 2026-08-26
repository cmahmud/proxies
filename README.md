# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 383
- HTTP: 123 alive / 68 gold
- HTTPS: 154 alive / 20 gold
- SOCKS4: 163 alive / 147 gold
- SOCKS5: 179 alive / 148 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39652
- Ever gold: 1300

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
