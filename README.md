# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 426
- HTTP: 104 alive / 77 gold
- HTTPS: 130 alive / 16 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 194 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42473
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
