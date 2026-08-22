# SyndProxy private pool

## Current pool

- Alive now: 915
- Gold now: 425
- HTTP: 278 alive / 93 gold
- HTTPS: 184 alive / 28 gold
- SOCKS4: 210 alive / 147 gold
- SOCKS5: 243 alive / 157 gold

## Historical pool

- Discovered: 162751
- Ever alive: 31547
- Ever gold: 1161

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
