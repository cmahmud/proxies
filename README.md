# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 405
- HTTP: 77 alive / 58 gold
- HTTPS: 63 alive / 18 gold
- SOCKS4: 176 alive / 164 gold
- SOCKS5: 191 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41573
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
