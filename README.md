# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 392
- HTTP: 91 alive / 65 gold
- HTTPS: 77 alive / 17 gold
- SOCKS4: 166 alive / 152 gold
- SOCKS5: 173 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41743
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
