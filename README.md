# SyndProxy validated proxy pool

## Current pool

- Alive now: 469
- Gold now: 393
- HTTP: 72 alive / 57 gold
- HTTPS: 41 alive / 13 gold
- SOCKS4: 175 alive / 158 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42846
- Ever gold: 1363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
