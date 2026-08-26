# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 381
- HTTP: 125 alive / 68 gold
- HTTPS: 161 alive / 20 gold
- SOCKS4: 162 alive / 146 gold
- SOCKS5: 178 alive / 147 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39663
- Ever gold: 1300

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
