# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 401
- HTTP: 93 alive / 59 gold
- HTTPS: 175 alive / 15 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 186 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41029
- Ever gold: 1316

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
