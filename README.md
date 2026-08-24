# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 378
- HTTP: 108 alive / 47 gold
- HTTPS: 48 alive / 9 gold
- SOCKS4: 174 alive / 157 gold
- SOCKS5: 182 alive / 165 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33540
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
