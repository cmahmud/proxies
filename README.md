# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 372
- HTTP: 91 alive / 45 gold
- HTTPS: 42 alive / 10 gold
- SOCKS4: 163 alive / 156 gold
- SOCKS5: 191 alive / 161 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32962
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
