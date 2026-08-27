# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 394
- HTTP: 102 alive / 59 gold
- HTTPS: 167 alive / 14 gold
- SOCKS4: 173 alive / 157 gold
- SOCKS5: 191 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41090
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
