# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 423
- HTTP: 99 alive / 73 gold
- HTTPS: 111 alive / 20 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 186 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42496
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
