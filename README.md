# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 418
- HTTP: 97 alive / 72 gold
- HTTPS: 116 alive / 18 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 193 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42483
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
