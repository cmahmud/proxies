# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 398
- HTTP: 76 alive / 57 gold
- HTTPS: 40 alive / 15 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42847
- Ever gold: 1363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
